use std::process::Command;

use assert_cmd::prelude::*;
use predicates::prelude::*;

use apd::版本号;

fn apd() -> Result<Command, Box<dyn std::error::Error>> {
    let cmd = Command::cargo_bin("apd")?;
    Ok(cmd)
}

#[test]
fn 无命令行参数() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("错误: 命令行格式错误"));

    Ok(())
}

#[test]
fn 未知命令() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.arg("666");
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("错误: 未知命令 666"));

    Ok(())
}

#[test]
fn help() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.arg("--help");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("用法:"));

    Ok(())
}

#[test]
fn 帮助() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.arg("--帮助");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("用法:"));

    Ok(())
}

#[test]
fn version() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.arg("--version");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains(版本号));

    Ok(())
}

#[test]
fn 版本() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = apd()?;

    cmd.arg("--版本");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains(版本号));

    Ok(())
}
