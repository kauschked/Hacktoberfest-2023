import { Socket } from 'net';
import { createCanvas, loadImage } from 'canvas';

const host: string = '127.0.0.1';
const port: number = 1234;

const MAX_X: number = 1285;
const MAX_Y: number = 725;

export async function mainSecond() {
    const socket = new Socket();
    socket.connect(port, host, () => {
        console.log('Connected to Pixelflut server.');
        socket.write('SIZE\n');
    });

    socket.on('data', (data: any) => {
        const message: string = data.toString();
        if (message.startsWith('SIZE')) {
            const answer: string[] = message.split(' ');
            console.log(`Detected size: ${answer[1]} x ${answer[2]}`);
            sendImageToServer(socket, 'src/deal-with-raccon.png');
        }
    });

    socket.on('error', (err) => {
        console.error('Socket error:', err);
    });
}

async function sendImageToServer(socket: Socket, imagePath: string) {
    const image = await loadImage(imagePath);
    const canvas = createCanvas(image.width, image.height);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(image, 0, 0, image.width, image.height);

    // Randomize starting X and Y based on the given ENV and the image size
    const startX = Math.floor(Math.random() * (MAX_X - image.width));
    const startY = Math.floor(Math.random() * (MAX_Y - image.height));

    let output: string = '';
    for (let x = 0; x < image.width; x++) {
        for (let y = 0; y < image.height; y++) {
            const pixel = ctx.getImageData(x, y, 1, 1).data;
            const hexColor = rgbToHex(pixel[0], pixel[1], pixel[2]);
            output += `PX ${startX + x} ${startY + y} ${hexColor}\n`;
        }
    }
    
    socket.write(output);
}

function rgbToHex(r: number, g: number, b: number): string {
    return ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

