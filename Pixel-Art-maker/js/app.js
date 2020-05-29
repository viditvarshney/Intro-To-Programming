// Grid mount function
function makeGrid() {

  // Storing grid height value
  const gridHeight = document.getElementById('height_in').value;
  // Storing grid width value
  const gridWidth = document.getElementById('width_in').value;
  // Storing table canvas
  const canvas = document.getElementById('pix_canvas');

  // Delete rows to start
  canvas.innerHTML = '';

  // Another way to delete rows
  // while (canvas.rows.length > 0) {
  //   canvas.deleteRow(0);
  // }

  // Loop to insert the rows
  for (let i = 0; i < gridHeight; i++) {
    let row = canvas.insertRow(i);

    // Loop to insert the cells
    for (let j = 0; j < gridWidth; j++) {
      let cell = row.insertCell(j);

      // Add click event to the cells
      cell.addEventListener('click', function(event) {
        // When the cell is clicked, the background color changes to the selected color
        event.target.style.backgroundColor = document.getElementById('colorPicker').value;
      });
    }
  }
}

// Add click event to the submit input
document.getElementById('sizePicker').addEventListener('submit', function(event) {
  event.preventDefault();
  // When the data is submitted the grid mount function is called
  makeGrid();
});