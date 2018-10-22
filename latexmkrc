@default_files = ("main.tex");
$pdf_mode = 1;
$latex_silent_switch = "-interaction=batchmode   -c-style-errors";
$silent = 1;

$aux_dir = "aux-files";
$out_dir = "output";

$view = 'none';

add_cus_dep('pytxcode','pytxmcr',0,'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }