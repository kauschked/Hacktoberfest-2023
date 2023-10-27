import { Socket } from 'net';

const host: string = '10.201.77.56';
const port: number = 4321;
const colors: string[] = ['00ff00', 'e28211', 'ff0000', '99b259', '0000ff'];
const xOffset: number = 50;
const yOffset: number = 50;
const cubeSize: number = 50;

async function main() {
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
            startPainting(socket);
        }
    });

    socket.on('error', (err) => {
        console.error('Socket error:', err);
    });
}

function startPainting(socket: Socket) {
    console.log('Painting...');
    let step: number = 0;

    setInterval(() => {
        const color: string = colors[step % colors.length];
        console.log(`Color: ${color}`);

        let output: string = '';
        for (let x = xOffset; x < xOffset + cubeSize; x++) {
            for (let y = yOffset; y < yOffset + cubeSize; y++) {
                output += `PX ${x} ${y} ${color}\n`;
            }
        }

        socket.write(output);
        step++;
    }, 500);
}

main();
