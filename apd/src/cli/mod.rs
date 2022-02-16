use std::env::Args;

pub enum 命令行参数 {
    // 解析错误
    错误(String),

    // --版本
    // --version
    版本,

    // --帮助
    // --help
    帮助,
    // TODO
}

impl 命令行参数 {
    pub fn new(arg: &mut Args) -> 命令行参数 {
        match arg.nth(1) {
            None => 命令行参数::命令行格式错误(),
            Some(命令) => match 命令.as_str() {
                "--版本" | "--version" => 命令行参数::版本,
                "--帮助" | "--help" => 命令行参数::帮助,
                // TODO
                _ => 命令行参数::错误(format!("未知命令 {}", 命令)),
            },
        }
    }

    pub fn 命令行格式错误() -> 命令行参数 {
        命令行参数::错误(format!("命令行格式错误 !  使用 \"--帮助\" 显示用法"))
    }
}

pub fn 显示帮助信息() {
    print!(
        "\
用法:
  apd --版本  显示版本信息
  apd --帮助  显示此帮助信息

TODO
"
    );
}
