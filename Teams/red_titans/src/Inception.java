import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.net.Socket;
import javax.imageio.ImageIO;

public class Inception {
  static String serverHost = "127.0.0.0";
  static int serverPort = 1234;
  public static void main(String[] args) throws IOException {
    BufferedImage image = ImageIO.read(
        new File("/usr/app/src/inception.png"));
    Socket socket = new Socket(serverHost,serverPort);
    OutputStream outputStream = socket.getOutputStream();
    BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(outputStream));
    //Thread für den fall das man noch einen parralel laufen lassen will um noch Schneller das Bild zu zeichnen
    // --> man muss das Bild davor Unterteilen damit die beiden Threads unabängig von einander Arbeiten
    Thread t1 = new Thread(() -> bildBuilder(image,socket,writer));
    t1.start();
  }

  public static void bildBuilder(BufferedImage image, Socket socket, Writer writer){
    try {
      int imageWidth = image.getWidth();
      int imageHeight = image.getHeight();
      for( int y = 0; y < imageHeight; y++){
        for (int x = 0; x < imageWidth; x++){
          int pixel = image.getRGB(x, y);
          int red = (pixel >> 16) & 0xFF;
          int green = (pixel >> 8) & 0xFF;
          int blue = pixel & 0xFF;
          int color = (red >> 16) + (green << 8) + blue;

          String command = String.format("PX %d %d %06X\n", x, y, color);
          writer.write(command);
          writer.flush();
        }
      }
      writer.close();
      socket.close();
    }catch (Exception e){
      System.out.println("Parralel1" + e.getMessage() +  e.getCause());
      e.printStackTrace();
      e.getMessage();
      e.getCause();
    }
  }
}
