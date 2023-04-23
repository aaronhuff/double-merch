fetch('data/traits_filters.json')
    .then(response => response.json())
    .then(data => {
        // code to display images based on filter categories
    });


function filterImages(category) {
    const images = document.querySelectorAll("#image-container img");
    images.forEach((img) => {
        const categoryData = data.categories.find(c => c.name === category);
        if (category === "All" || categoryData.images.includes(img.src.split('/').pop())) {
            img.style.display = "block";
        } else {
            img.style.display = "none";
        }
    });
}

const filterBtns = document.querySelectorAll(".filter-btn");
filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        filterImages(btn.dataset.category);
    });
});

filterImages("all");

data.traits.forEach((category) => {
    const button = document.createElement("button");
    button.classList.add("filter-btn");
    button.dataset.category = category.name;
    button.innerText = category.name;
    document.getElementById("filter-buttons").appendChild(button);
  });