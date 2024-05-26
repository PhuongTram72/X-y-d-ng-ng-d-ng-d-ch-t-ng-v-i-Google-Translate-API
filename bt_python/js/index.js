document.addEventListener("DOMContentLoaded", function () {
  console.log("Đã tải xong index.js");
});

function fetchTextData(action, callback) {
  fetch(`http://localhost/bt_python/api.php?action=${action}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((json_data) => {
      callback(json_data);
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

function updateTable(data) {
  let tableHTML = `
    <table class="table table-bordered table-success">
      <thead>
        <tr>
          <th>STT</th>
          <th>Text</th>
          <th>Language</th>
        </tr>
      </thead>
      <tbody>`;
  
  data.forEach((item, index) => {
    tableHTML += `
      <tr>
        <td>${index + 1}</td>
        <td>${item.text}</td>
        <td>${item.language}</td>
      </tr>`;
  });

  tableHTML += `</tbody></table>`;
  document.getElementById("table_now").innerHTML = tableHTML;
}

function refreshData() {
  fetchTextData("get_all", (data) => {
    updateTable(data);
  });
}

refreshData();
setInterval(refreshData, 1000 * 60); // Cập nhật mỗi 1 phút
