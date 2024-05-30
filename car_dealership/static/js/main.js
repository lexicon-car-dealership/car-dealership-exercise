document.addEventListener('DOMContentLoaded', function () {
  const filterForm = document.getElementById('filter_form');
  const searchInput = document.getElementById('filter_form_search');

  searchInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      const urlParams = new URLSearchParams(new FormData(filterForm));
      const searchQuery = searchInput.value;
      urlParams.set('search', searchQuery);
      window.location.href = `${filterForm.action}?${urlParams.toString()}`;
    }
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
