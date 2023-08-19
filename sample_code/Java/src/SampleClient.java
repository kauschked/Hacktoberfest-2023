import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.List;

public class SampleClient {

  private static final String host = "127.0.0.1";
  private static final int port = 1234;
  private static final List<String> colors = List.of("00ff00", "e28211", "ff0000", "99b259", "0000ff");
  private static final int xOffset = 10;
  private static final int yOffset = 10;
  private static final int cubeSize = 5;

  public static void main(String[] args) throws IOException, InterruptedException {

    try (final Socket s = new Socket(host, port)) {

      System.out.println("Connected to Pixelflut server.");
      final PrintWriter writer = new PrintWriter(s.getOutputStream());
      final InputStreamReader streamReader = new InputStreamReader(s.getInputStream());
      final BufferedReader reader = new BufferedReader(streamReader);

      writer.println("SIZE");
      writer.flush();
      final String[] answer = reader.readLine().split(" ");
      System.out.printf("Detected size: %s x %s%n", answer[1], answer[2]);

      System.out.println("Painting...");
      int step = 0;
      while (true) {
        final String color = colors.get(step % colors.size());
        System.out.printf("Color: %s\n", color);
        final StringBuilder output = new StringBuilder(cubeSize * cubeSize);
        for (int x = xOffset; x < xOffset + cubeSize; x++) {
          for (int y = yOffset; y < yOffset + cubeSize; y++) {
            output.append(String.format("PX %d %d %s\n", x, y, color));
          }
        }
        writer.print(output);
        writer.flush();
        Thread.sleep(500);
        step++;
      }
    }
  }
}
