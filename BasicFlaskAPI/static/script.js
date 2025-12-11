// Load all products
function loadProducts() {
    fetch("/api/products")
        .then(res => res.json())
        .then(data => {
            let table = document.getElementById("productTable");
            table.innerHTML = `
                <tr>
                    <th>ID</th><th>Name</th><th>Price</th><th>Action</th>
                </tr>
            `;
            data.forEach(p => {
                table.innerHTML += `
                    <tr>
                        <td>${p.id}</td>
                        <td>${p.name}</td>
                        <td>${p.price}</td>
                        <td>
                            <button onclick="deleteProduct(${p.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

// Add Product
function addProduct() {
    let name = document.getElementById("name").value;
    let price = document.getElementById("price").value;

    fetch("/api/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, price })
    })
    .then(() => loadProducts());
}

// Delete Product
function deleteProduct(id) {
    fetch(`/api/products/${id}`, { method: "DELETE" })
        .then(() => loadProducts());
}

// Load products on startup
loadProducts();
