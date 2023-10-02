const { MongoClient } = require("mongodb");
const database = 'e-comm';
// Replace the uri string with your connection string.
const uri = "mongodb://127.0.0.1:27017";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();
    const db = client.db(database);
    const products = db.collection('products');

    // Query for a product that has the name 'm 21'
    const query = { name: 'pocoM5' };
    const product = await products.findOne(query);

    console.log(product);
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

run().catch(console.dir);
