# Edit-Video-Date-Metadata-yt-dlp
Edit Video Date Metadata with exiftool and a python scrip after each video has downloaded with yt-dlp.

Get [yt-dlp](https://github.com/yt-dlp/yt-dlp)
Get [ExifTool](https://exiftool.org/)

After Video Downloaded with yt-dlp Run py script for exiftool to change date.

Add this argument/switch to your yt-dlp command:
```sh
  --exec "python \"C:\\path\\to\\your\\script\\scriptModifyDate.py\" %(filename)q '%(upload_date)s' 'NA'"
```
