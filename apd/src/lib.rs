use anyhow::Result;
//use log::info;
//use anyhow::Context;

use cli::命令行参数;
use cli::显示帮助信息;

pub mod cli;
mod db;

#[cfg(test)]
mod test;

// 版本号
pub const 版本号: &str = "apd 0.1.0-a1";

pub fn 执行命令(参数: &命令行参数) -> Result<()> {
    match 参数 {
        命令行参数::错误(错误信息) => {
            eprintln!("错误: {}", 错误信息);
            std::process::exit(1);
        }
        命令行参数::版本 => {
            println!("{}", 版本号);
            println!("sqlite {}", db::sqlite_version());
        }
        命令行参数::帮助 => 显示帮助信息(),
        // TODO
    }

    Ok(())
}
