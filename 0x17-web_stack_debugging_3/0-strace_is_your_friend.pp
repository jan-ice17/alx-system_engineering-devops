# Define the file to edit
$file_to_edit = '/var/www/html/wp-settings.php'

# Replace the line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin'],
}

