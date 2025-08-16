<script>
  function showDescription(id) {
    // Hide all description divs if there are multiple later
    var descriptions = document.querySelectorAll('.description');
    descriptions.forEach(desc => desc.style.display = 'none');

    // Show the clicked one
    document.getElementById(id).style.display = 'block';
  }
</script>
