document.addEventListener('DOMContentLoaded', function () {
  const profileDropdown = document.getElementById('navbarDropdown');
  if (profileDropdown) {
    const menuBar = document.getElementById('menu-bar');
    profileDropdown.addEventListener('click', () => {
      menuBar.classList.toggle('active');
    });
  }
  //filters
  const filterButton = document.getElementById('filter-toggle');
  const navSearchFilters = document.getElementById('nav-search-filters');
  const isFilterActive = window.localStorage.getItem('filtertab') === 'true';
  if (isFilterActive) navSearchFilters.classList.add('active');

  filterButton.addEventListener('click', event => {
    event.preventDefault();
    const isFilterActive = navSearchFilters.classList.toggle('active');
    window.localStorage.setItem('filtertab', isFilterActive);
  });
});
  document
    .getElementById("search-input")
    .addEventListener("input", function () {
      const searchQuery = this.value.toLowerCase();
      const items = document.querySelectorAll("#item-list .list-group-item");
      let hasResults = false;

      items.forEach((item) => {
        if (item.textContent.toLowerCase().includes(searchQuery)) {
          item.style.display = "";
          hasResults = true;
        } else {
          item.style.display = "none";
        }
      });

      document.getElementById("no-results").style.display = hasResults
        ? "none"
        : "";
    });

  document
    .getElementById("create-new-link")
    .addEventListener("click", function () {
      const searchQuery = document.getElementById("search-input").value;
      const manufacturerNameInput = document.querySelector(
        '#add-manufacturer-form input[name="name"]'
      );
      if (manufacturerNameInput) {
        manufacturerNameInput.value = searchQuery;
      }
    });
