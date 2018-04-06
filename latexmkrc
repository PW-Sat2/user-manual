@default_files = ("main.tex");
$pdf_mode = 1;

$aux_dir = "aux-files";
$out_dir = "output";

$view = 'none';

add_cus_dep('pytxcode','pytxmcr',0,'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }