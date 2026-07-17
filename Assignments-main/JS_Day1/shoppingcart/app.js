// Load JSON data
const products = require("./products.json");

// Activity 1 - Display Product Names (forEach)
console.log("\nActivity 1 - Display Product Names");

products.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
});


// Activity 2 - Calculate Total Price (map)
console.log("\nActivity 2 - Calculate Total Price");

const totalPrice = products.map(product => ({
    name: product.name,
    totalPrice: product.price * product.quantity
}));

console.log(totalPrice);


// Activity 3 - Find Available Products (filter)
console.log("\nActivity 3 - Find Available Products");

const availableProducts = products.filter(product => product.inStock);

console.log(availableProducts);


// Activity 4 - Find Expensive Products (filter)
console.log("\nActivity 4 - Find Expensive Products (> ₹5000)");

const expensiveProducts = products.filter(product => product.price > 5000);

console.log(expensiveProducts);


// Activity 5 - Search for a Product (find)
console.log("\nActivity 5 - Search for a Product");

const searchProduct = products.find(product => product.id === 103);

console.log(searchProduct);


// Activity 6 - Check Product Availability (some)
console.log("\nActivity 6 - Check Product Availability");

const checkAvailability = products.some(product => !product.inStock);

if (checkAvailability) {
    console.log("Yes, some products are out of stock.");
} else {
    console.log("All products are available.");
}


// Activity 7 - Verify Stock Status (every)
console.log("\nActivity 7 - Verify Stock Status");

const allAvailable = products.every(product => product.inStock);

console.log("All products available:", allAvailable);


// Activity 8 - Calculate Grand Total (reduce)
console.log("\nActivity 8 - Calculate Grand Total");

const grandTotal = products.reduce((total, product) => {
    return total + (product.price * product.quantity);
}, 0);

console.log("Grand Total = ₹" + grandTotal);


// Activity 9 - Sort Products by Price (sort)
console.log("\nActivity 9 - Sort Products by Price");

const sortedProducts = [...products].sort((a, b) => a.price - b.price);

sortedProducts.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
});


// Activity 10 - Display Only Product Names (map)
console.log("\nActivity 10 - Display Only Product Names");

const productNames = products.map(product => product.name);

console.log(productNames);


// Activity 11 - Find Product Position (findIndex)
console.log("\nActivity 11 - Find Product Position");

const index = products.findIndex(product => product.name === "Office Chair");

console.log(index);


// Activity 12 - Remove Out-of-Stock Products (filter)
console.log("\nActivity 12 - Remove Out-of-Stock Products");

const availableCart = products.filter(product => product.inStock);

console.log(availableCart);


// Activity 13 - Add GST (18%) (map)
console.log("\nActivity 13 - Add GST (18%)");

const productsWithGST = products.map(product => ({
    ...product,
    gst: product.price * 0.18
}));

console.log(productsWithGST);


// Activity 14 - Top 3 Cheapest Products
console.log("\nActivity 14 - Top 3 Cheapest Products");

const cheapProducts = [...products]
    .sort((a, b) => a.price - b.price)
    .slice(0, 3);

cheapProducts.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
});


// Activity 15 - Generate Bill Summary (reduce)
console.log("\nActivity 15 - Generate Bill Summary");

const billSummary = products.reduce((summary, product) => {

    summary.totalProducts++;
    summary.totalQuantity += product.quantity;
    summary.totalAmount += product.price * product.quantity;

    return summary;

}, {
    totalProducts: 0,
    totalQuantity: 0,
    totalAmount: 0
});

console.log(billSummary);
