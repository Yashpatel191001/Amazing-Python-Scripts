const {MongoClient} = require('mongodb');
const url = "mongodb://127.0.0.1:27017";
const databaseName='e-comm';
const client= new MongoClient(url);

async function dbConnect(){
    let result = await client.connect();
    let db = result.db(databaseName);
    return db.collection('products');
    // let response = await collection.find({}).toArray();
    // console.log(response);
}

module.exports = dbConnect;


// const main = async () =>{
//     let data = await dbConnect();
//     data =await data.find().toArray();
//     console.warn(data);
// }
// main();
