on run
	try
		-- Locate source folder inside the mounted DMG
		tell application "Finder"
			set parentFolder to POSIX path of ((container of (path to me)) as alias)
		end tell
		
		-- Target user directory: ~/Library/Dictionaries/
		set targetDir to (POSIX path of (path to library folder from user domain)) & "Dictionaries"
		
		-- Ensure ~/Library/Dictionaries exists without needing root/sudo
		do shell script "/bin/mkdir -p " & quoted form of targetDir
		
		-- Copy dictionary bundles
		set dict1 to parentFolder & "Mongolian-English-Altangerel.dictionary"
		set dict2 to parentFolder & "Mongolian-Tsevel-Explanatory.dictionary"
		
		do shell script "/bin/cp -R " & quoted form of dict1 & " " & quoted form of targetDir & "/ && /bin/cp -R " & quoted form of dict2 & " " & quoted form of targetDir & "/"
		
		-- Touch destination directory so macOS Dictionary Services immediately recognizes the changes
		do shell script "/usr/bin/touch " & quoted form of targetDir
		
		-- Show success notification dialog
		display dialog "🇲🇳 Монгол толь бичгүүд амжилттай суулаа!" & return & return & "Суулгасан зам: ~/Library/Dictionaries/" & return & return & "Дараагийн алхам: Dictionary.app нээгдэх үед Settings (Cmd + ,) цонхноос шинэ толиудыг чеклэж идэвхжүүлнэ үү." with title "Монгол хэлний толь бичиг" buttons {"Dictionary нээх", "Болсон"} default button 1 with icon note
		
		if button returned of result is "Dictionary нээх" then
			tell application "Dictionary" to activate
		end if
	on error errMsg
		display alert "Суулгахад алдаа гарлаа" message errMsg as critical
	end try
end run
