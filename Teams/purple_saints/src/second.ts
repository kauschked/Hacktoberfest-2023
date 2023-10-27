import { Socket } from 'net';
import { createCanvas, loadImage } from 'canvas';

const host: string = '127.0.0.1';
const port: number = 1234;
/* 
const host: string = '10.201.77.56';
const port: number = 4321; */


const MAX_X: number = 0;
const MAX_Y: number = 0;

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
    const canvas = createCanvas(MAX_X, MAX_Y);
    const ctx = canvas.getContext('2d');

    let startX = MAX_X;
    let startY = MAX_Y;

    let direction = -5;

    setInterval(() => {
        ctx.fillStyle = 'black';
        ctx.fillRect(startX, startY, image.width, image.height);
        startY += direction;
        if (startY <= 0 || startY + image.height >= MAX_Y) {
            direction = -direction;
        }
        ctx.drawImage(image, startX, startY, image.width, image.height);
        sendCanvasData(socket, ctx);

    }, 100);
}




function sendCanvasData(socket: Socket, ctx: any) {
    let output: string = '';
    for (let x = 0; x < MAX_X; x++) {
        for (let y = 0; y < MAX_Y; y++) {
            const pixel = ctx.getImageData(x, y, 1, 1).data;
            if (pixel[3] !== 0) { // If pixel is not transparent
                const hexColor = rgbToHex(pixel[0], pixel[1], pixel[2]);
                output += `PX ${x} ${y} ${hexColor}\n`;
            }
        }
    }
    socket.write(output);
}

function rgbToHex(r: number, g: number, b: number): string {
    return ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

