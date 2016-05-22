<?php

# The client script

# create our gearman client
$gmc= new GearmanClient();

# add the default job server
$gmc->addServer();

# set a couple of callbacks so we can track progress
$gmc->setCompleteCallback("reverse_complete");
$gmc->setStatusCallback("reverse_status");

# add a task for the "reverse" function
$task= $gmc->addTask("reverse", "Hello World!", null, "1");

# add another task, but this one to run in the background
$task= $gmc->addTaskBackground("reverse", "!dlroW olleH", null, "2");

if (! $gmc->runTasks())
{
    echo "ERROR " . $gmc->error() . "\n";
    exit;
}

echo "DONE\n";

function reverse_status($task)
{
    echo "STATUS: " . $task->unique() . ", " . $task->jobHandle() . " - " . $task->taskNumerator() . 
         "/" . $task->taskDenominator() . "\n";
}

function reverse_complete($task)
{
    echo "COMPLETE: " . $task->unique() . ", " . $task->data() . "\n";
}

?> 