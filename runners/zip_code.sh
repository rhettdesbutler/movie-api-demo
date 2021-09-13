filename=$1
codepath=$2
work_dir=$PWD

zip -r $work_dir/zipped_code/$filename.zip $codepath
