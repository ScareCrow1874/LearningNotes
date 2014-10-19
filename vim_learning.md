My vim learning

-good: repeat cmds
-bad:two modes, and too complicated keyboard

Basic commands:

1) Insert Mode (i to get into)
	to insert some characters repeatedly in insert Mode, do <C-o>+num+i+'the char'<Esc>
	If you are in Command mode, do <Ese>num+i+'the char'<Ese>
2) Comand Mode (Esc to exit)
   :w Save
   :q Quit
   :q! Quit w/o saving
   
   You can type several of these commands on the same line

   Moving cursor: 
   	h - left; j - down; k - up; l - right;
   Deleting text in CMD mode: type 'x';

   Word movement: 
   	w - start of next word; 
   	e - end of word; b - beginning of word
   	
	Repeat...
	3w : move 3 words;
	9l : move 9 chars;

   Find a character with f and F:
   	fo will find o;
	
   Go to matching parentheses, just use %

   Go to the beginning of the file: gg
   Go to the end of the file: G

   Search: /xxx; Next/prev found: type n or N

   Deleting: d;
       Delete 2 words: d2w;
       This command will copy the text you deleted, and you can paste it somewhere pressing 'p'

       Delete the whole line: dd; 2dd for deleting 2 lines

   Undo:
	Press u to undo the last commands, U to fix a whole line


   **
   Repitition with . : just press '.'

   Cut/Copy and paste:
       Position the cursor where you want to begin cutting;
       Press v (V for cutting the whole line)
       Move the cursor to the end of what you want to cut
       Press d to cut or y to copy
       Move to where you would like to paste
       Press P to paste before the cursor, p for after the cursor

   
   To insert the contents of a file, type :r FILENAME

   To have visual selection, type v
   
   ---Several commands involving files
   v motion :w FILENAME saves the visually selected lines in file FILENAME

   :r FILENAME retrieves disk file FILENAME and puts it below the cursor position
   
   :r !dir reads the output of the dir command and puts it below the cursor position

   GENERALLY, execute an external command, do :! followed by the external cmd

3) Other tips:
   To display line nubmers, do :set nu or :set numbers
