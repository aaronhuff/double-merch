let images = [];
let currentPage = 1;
let imagesPerPage = 12;

// Load filters from JSON file
fetch('data/filters.json')
    .then(response => response.json())
    .then(filters => {
        // Create a button for each filter
        const buttonsDiv = document.getElementById('buttons');
        filters.traits.forEach(filter => {
            const button = document.createElement('button');
            button.textContent = filter.name;
            button.className = 'btn btn-light btn-sm';
            button.type = 'button';
            button.addEventListener('click', () => {
                displayImages(filter);
            });
            buttonsDiv.appendChild(button);
        });
    });

function displayImages(filter) {
    // Load images for selected filter
    images = filter.images;

    // Show first page of images and render pagination buttons
    currentPage = 1;
    showPage(currentPage);
    renderPagination();
}


// Show a specific page of images
function showPage(page) {
    const startIndex = (page - 1) * imagesPerPage;
    const endIndex = startIndex + imagesPerPage;
    const pageImages = images.slice(startIndex, endIndex);

    const pagesDiv = document.getElementById('pages');
    while (pagesDiv.firstChild) {
        pagesDiv.removeChild(pagesDiv.firstChild);
    }
    const pageDiv = document.createElement('div');
    pageDiv.classList.add('page');

    pageImages.forEach((image, index) => {
        const img = document.createElement('img');
        img.className = 'image rounded';
        img.src = image;
        img.alt = image.split('.')[0];
        img.id = `image-${startIndex + index}`;
        pageDiv.appendChild(img);
    });

    pagesDiv.appendChild(pageDiv);
    setActivePage(page);
}

// Render pagination buttons
function renderPagination() {
    const paginationDiv = document.querySelector('.pagination');
    paginationDiv.innerHTML = '';

    const pageCount = Math.ceil(images.length / imagesPerPage);

    for (let i = 1; i <= pageCount; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        button.className = 'btn btn-light btn-sm';
        button.addEventListener('click', () => {
            showPage(i);
        });
        paginationDiv.appendChild(button);
    }
}

// Set active page button
function setActivePage(page) {
    const buttons = document.querySelectorAll('.pagination button');
    buttons.forEach(button => {
        if (parseInt(button.textContent) === page) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });
}
