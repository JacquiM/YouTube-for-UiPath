# YouTube for UiPath

The package allows users to interact with YouTube through UiPath which encapsulates a Python script which handles the heavy-lifting integration. The Python script takes in operational parameters (parameters that ensure the script works the way it should) and authentication parameters (parameters needed to authenticate to the YouTube API service).
<p align="center">
<img src="https://github.com/jacquim/YouTube-for-UiPath/blob/main/Youtube%20Playlists.png" title="YouTube Playlist Integration Architecture">
</p>

The library currently only allows for the following functionality:
* <b>Get Playlist Items from YouTube</b>
  * Operational Parameters:
    - <i>File path:</i> The path of the Excel file to be stored, containing the playlist items. Should be of the type *.xlsx
    - <i>Playlist ID:</i> The ID of the playlist from which items are to be extracted. The ID can be found in the playlist URL when navigating to the playlist on YouTube (https://www.youtube.com/watch?v=v34-kepOHF4&list=<b><u>PLtcIogydu_Bqb9Hgi1ULhCyJRTb27Fdee</u></b>)
  * Authentication Parameter:
    - <i>Developer Key:</i> The developer key can be obtained from the <a href="https://console.developers.google.com" tagret="_blank>Google Developer Console</a> The developer key should also be associated to the YouTube API. For more information on how to get that setup, <a href="https://thejpanda.com/2021/01/21/automation-youtube-playlist-monitoring-using-python/" target="_blank">read this post</a>.

This library is a work in progress and is open for collaboration on <a href="https://github.com/JacquiM/YouTube-for-UiPath/" target="_blank">GitHub</a>. 

<b>Please Note:</b> This vb.net package was created in UiPath Studio and as such, the recommended consumption interface (interface that uses the library) is UiPath. There is no guarantee that this will work outside of UiPath - it'd be interesting to get feedback about whether it does or not - but still... No promises. 
