function handleSearch() {
    var query = document.getElementById('searchInput').value;
    // Redirect to Google with the search query
    window.location.href = 'https://www.google.com/search?q=' + encodeURIComponent(query);
    return false; // Prevent form submission
}
