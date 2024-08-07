const express = require('express');
const app = express();

const fn = () => {
    let items = [];

    for (let i = 0; i < 99999995; i++) {
        items.push(i);
    }
}

app.get('/', (req, res) => {
    // Allocate 2GB of memory

    res.send(list);
});

const port = 8080;
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
    fn();
    console.log('continue');
});