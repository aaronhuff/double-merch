let images = [];
let currentPage = 1;
let imagesPerPage = 8;

// Load filters from JSON file
fetch('data/filters.json')
    .then(response => response.json())
    .then(filters => {
        // Create a button for each filter
        const buttonsDiv = document.getElementById('buttons');
        filters.traits.forEach(filter => {
            const button = document.createElement('button');
            button.textContent = filter.name;
            button.className = 'button btn btn-light btn-sm';
            button.type = 'button';
            button.addEventListener('click', () => {
                displayImages(filter);
            });
            buttonsDiv.appendChild(button);
            if (filter.name = "All")
            {
                displayImages(filter);
            }
        });
    });



function displayImages(filter) {
    // Load images for selected filter
    images = filter.images;

    // Show first page of images and render pagination buttons
    currentPage = 1;
    showPage(currentPage);
    renderPagination();
    setActiveFilter(filter);
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
    pageDiv.className = 'page flex-container';

    pageImages.forEach((image, index) => {
        const imageDiv = document.createElement('div');
        imageDiv.className = 'bear flex-container';

        const img = document.createElement('img');
        img.className = 'image rounded';
        img.src = image;
        img.alt = image.split('/').pop().split('.')[0];
        img.id = `image-${startIndex + index}`;
        imageDiv.appendChild(img);

        const label = document.createElement('label');
        label.textContent = `Bear #${img.alt}`;
        label.className = 'label other';
        imageDiv.appendChild(label)

        pageDiv.appendChild(imageDiv);
    });

    pagesDiv.appendChild(pageDiv);
    setActivePage(page);
}

// Render pagination buttons
function renderPagination() {
    const paginationDiv = document.querySelector('.pagination');
    paginationDiv.className = 'pagination flex-container';
    paginationDiv.innerHTML = '';

    const pageCount = Math.ceil(images.length / imagesPerPage);

    for (let i = 1; i <= pageCount; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        button.className = 'button btn btn-light btn-sm';
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

// Set active filter button
function setActiveFilter(filter) {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        if (parseInt(button.textContent) === filter.name) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });
}