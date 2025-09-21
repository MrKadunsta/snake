// Get the table and its rows
const table = document.getElementById('highscoreTable');
const rows = Array.from(table.querySelectorAll('tr'));

// Reverse the order of the rows array
rows.reverse();

// Re-append the rows to the table in the new order
rows.forEach(row => table.appendChild(row));

const targetRowCount = 5; // desired number of data rows (excluding header)
const headerOffset = 1;

function adjustTableRows() {
    let currentRows = table.rows.length - headerOffset;

    // Remove extra rows
    while (currentRows > targetRowCount) {
        table.deleteRow(table.rows.length - 1);
        currentRows--;
    }
}

// Observe table changes in real-time
const observer = new MutationObserver(adjustTableRows);
observer.observe(table, { childList: true });

adjustTableRows(); // initial adjustment

function swapCells() {
  let pos1 = document.getElementById("pos1");
  let pos2 = document.getElementById("pos2");
  let pos4 = document.getElementById("pos4");
  let pos5 = document.getElementById("pos5");

  let temp1 = pos1.innerHTML;
  let temp2 = pos2.innerHTML;
  let temp4 = pos4.innerHTML;
  let temp5 = pos5.innerHTML;

  pos1.innerHTML = pos5.innerHTML;
  pos2.innerHTML = pos4.innerHTML;
  pos4.innerHTML = pos2.innerHTML;
  pos5.innerHTML = pos1.innerHTML;


  pos1.innerHTML = temp5;
  pos2.innerHTML = temp4;
  pos4.innerHTML = temp2;
  pos5.innerHTML = temp1;
}

// Run automatically when page loads
window.onload = swapCells;