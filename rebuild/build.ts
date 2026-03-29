import * as fs from 'fs';

function greet(name: any): string {
    return "Hello, ".concat(name, "!");
}

const message: string = greet("World");
console.log(message);

const exampleFileContent = fs.readFileSync('.gitignore','utf8');
console.log(exampleFileContent);