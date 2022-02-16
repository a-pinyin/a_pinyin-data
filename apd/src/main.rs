use anyhow::Result;
use env_logger::Env;

use apd::cli::命令行参数;
use apd::执行命令;

fn main() -> Result<()> {
    // 初始化 env_logger 默认日志级别: info
    env_logger::Builder::from_env(Env::default().default_filter_or("info")).init();

    let 参数 = 命令行参数::new(&mut std::env::args());
    执行命令(&参数)
}
