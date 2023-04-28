function populateTable(streams) {
  var table = document.getElementById('download-table');
  var tbody = table.getElementsByTagName('tbody')[0];

  for (var i = 0; i < streams.length; i++) {
    var stream = streams[i];

    var quality = stream.resolution + 'p';
    var filetype = stream.mime_type.split('/')[1];
    var downloadLink =
      "{{ url_for('download_video', url=url, itag=stream.itag) }}";
    var status = '<a href="' + downloadLink + '">Download</a>';

    var row = tbody.insertRow(i);
    var qualityCell = row.insertCell(0);
    var filetypeCell = row.insertCell(1);
    var statusCell = row.insertCell(2);

    qualityCell.innerHTML = quality;
    filetypeCell.innerHTML = filetype;
    statusCell.innerHTML = status;
  }
}
