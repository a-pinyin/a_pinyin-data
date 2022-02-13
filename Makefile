# a_pinyin-data 编译脚本
#
# 使用 make 是为了辅助自动化编译, 方便 CI 和本地开发.
#
# 本 Makefile 的使用方式主要有:
#
# + make
#   默认目标, 或者: make out
#   用于开发者手动编译 apd 工具, 以及生成内置数据库 a_pinyin-2.zip
#
# + make apd
#   仅编译 apd 工具
#
# + make ci
#   用于 github CI, 含代码检查, 测试等

# 配置变量

# cargo 可执行命令位置
BIN_CARGO := cargo
# zip 可执行命令
BIN_ZIP := zip

# 命令前缀
PREFIX :=


# [导出] 默认 make 目标, 编译 apd 工具及生成内置数据库
# 用于开发者手动编译: make out
.PHONY: out
out: apd db2

# [导出] 用于 github CI: make ci
.PHONY: ci
ci: first_test check test out

# [导出] 用于编译 apd: make apd
.PHONY: apd
apd: apd_release


#### 下方是具体的编译命令

# DEBUG 用于测试 ${PREFIX`}
.PHONY: first_test
first_test:
	echo ${PREFIX}
	${PREFIX} echo 666

# 编译 apd 工具 (release)
.PHONY: apd_release
apd_release:
	cd apd && ${PREFIX} ${BIN_CARGO} build --release

# 测试
.PHONY: test
test: test_apd

.PHONY: test_apd
test_apd:
	cd apd && ${PREFIX} ${BIN_CARGO} test


# 源代码检查, 用于 CI
.PHONY: check
check: check_apd

# cargo fmt
.PHONY: check_apd
check_apd:
	cd apd && ${PREFIX} ${BIN_CARGO} fmt --check


# TODO 生成内置数据库 a_pinyin-2.zip
.PHONY: db2
db2:
	echo TODO
	mkdir -p out
	touch out/a_pinyin-2.zip