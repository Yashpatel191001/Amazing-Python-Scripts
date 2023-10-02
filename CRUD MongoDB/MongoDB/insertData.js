const dbConnect = require('./mongodb'); 

const insert = async () => {
    const db = await dbConnect();
    const result = await db.insertMany([
        { name: 'nord1', price: 20000, brand: '1+', category: 'mobile' },
        { name: 'nord2', price: 20000, brand: '1+', category: 'mobile' },
        { name: 'nord3', price: 20000, brand: '1+', category: 'mobile' }
    ]);
    if(result.acknowledged){
        console.log("data inserted");
    } // You may want to log or handle the result here
};

insert();