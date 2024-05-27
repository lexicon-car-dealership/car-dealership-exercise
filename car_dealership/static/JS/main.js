document.addEventListener('DOMContentLoaded', function () {
  const filterForm = document.getElementById('filter_form');
  const brandDropdown = document.getElementById('brand_select');
  const modelDropdown = document.getElementById('model_select');
  const searchInput = document.getElementById('filter_form_search');

  const filters = [
    brandDropdown,
    modelDropdown,
    document.getElementById('fuel_select'),
    document.getElementById('filter_form_year'),
    document.getElementById('filter_form_minPrice'),
    document.getElementById('filter_form_maxPrice'),
  ];

  filters.forEach(filter => {
    filter.addEventListener('change', function () {
      filterForm.submit();
    });
  });

  brandDropdown.addEventListener('change', function () {
    const brand = this.value;
    if (brand) {
      fetch(`/get-models/?brand=${brand}`)
        .then(response => response.json())
        .then(data => {
          modelDropdown.innerHTML = '<option value="">Select Model</option>';
          data.models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            modelDropdown.appendChild(option);
          });
          modelDropdown.disabled = false;
        });
    } else {
      modelDropdown.innerHTML = '<option value="">Select Model</option>';
      modelDropdown.disabled = true;
    }
    filterForm.submit();
  });

  searchInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      const urlParams = new URLSearchParams(new FormData(filterForm));
      const searchQuery = searchInput.value;
      urlParams.set('search', searchQuery);
      window.location.href = `${filterForm.action}?${urlParams.toString()}`;
    }
  });

  if (brandDropdown.value) {
    const brand = brandDropdown.value;
    fetch(`/get-models/?brand=${brand}`)
      .then(response => response.json())
      .then(data => {
        modelDropdown.innerHTML = '<option value="">Select Model</option>';
        data.models.forEach(model => {
          const option = document.createElement('option');
          option.value = model;
          option.textContent = model;
          modelDropdown.appendChild(option);
        });
        modelDropdown.disabled = false;
        if ('{{ request.GET.model }}') {
          modelDropdown.value = '{{ request.GET.model }}';
        }
      });
  }
});
