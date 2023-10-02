const express = require('express');
const Product = require('./product');
const mongoose = require('mongoose'); // Use the regular import

require('./config');
const app = express();
app.use(express.json());

app.get("/search/:key", async (req, res) => {
    let search = req.params.key;
    let data = await Product.find({
        "$or": [
            { "name": { $regex: req.params.key } },
            { "brand": { $regex: req.params.key } }
        ]
    });
    res.send(data);
});

app.listen(9000);
