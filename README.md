# Code Commenter
Generate stylized code comment headers to help make your code more readable

## Basic Usage
To print a comment header to the console run
```bash
generate-comment -t My_Script_Heading
```
and if you wish to have it copied to your clipboard, add the `-c` flag
```bash
generate-comment -t My_Script_Heading -c
```
Code commenter supports multiple language comments. The default is Python but if you wish to generate a comment for example, Golang, set the `-lang` flag.
```bash
generate-comment -t My_Script_Heading -lang GO
```
