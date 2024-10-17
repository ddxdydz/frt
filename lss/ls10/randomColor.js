function getRandomColor(){
    const R = Math.random() * 255;
    const G = Math.random() * 255;
    const B = Math.random() * 255;
    
    return `rgb(${R},${G},${B})`;
}