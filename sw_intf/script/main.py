from ..src import parse_qemu_log

if __name__ == '__main__':
    in_dir = "db/lenet_raw"
    workload = parse_qemu_log.Workload(
        in_dir=in_dir,
        in_compilation=True,
        use_real_data=False,
        dump_results=False)
