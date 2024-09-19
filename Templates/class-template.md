<%*
const fileNameDate = tp.date.now("YYYY-MM-DD--HH-mm")
const Folder = "Universidade"
await tp.file.create_new("","Meeting--" + fileNameDate,true)
await tp.file.move(Folder)
%>