# whisperx-videogrep-workflow
Helper scripts for WhisperX transcription for videogrep editing

## main workflow
- install whisperx (separate conda container recommended)
- install videogrep (separate conda container recommended)
- run **whisper.bat sourcefile.mp4** (container with whisperx)
- run **python convert-whisperx-json.py sourcefile** (any container)
- edit **vgrep.bat** for search words and export (defaults to .xml)
- run **vgrep.bat sourcefile** (container with videogrep)
- davinci resolve does not support absolute file urls so edit **sourcefile_clips.xml** and find&replace all **\<pathurl\>file://C:\editpath\sourcefile.mp4\</pathurl\>** to be **\<pathurl\>file://sourcefile.mp4\</pathurl\>**

## misc
- **remux.bat** for trivial remuxing (twitch captures are often actually transportstreams which are incorrectly muxed and unsupported)
- **whispersrt.py** is an old script for creating a .srt file from whisperx. possibly broken, included only because i made it for some reason and left sitting in the dir.
