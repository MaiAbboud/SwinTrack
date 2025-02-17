import argparse
import config.global_path as gp

def get_train_args_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--method_name', default = 'SwinTrack', type=str, help='Method name')
    parser.add_argument('--config_name', default = 'Tiny', type=str, help='Config name')
    # parser.add_argument('--mixin_config', type=str, action='append')
    # parser.add_argument('--mixin_config', default= 'tracking.yaml', type=str, action='append')
    parser.add_argument('--mixin_config', default= 'evaluation.yaml', type=str, action='append')
    # parser.add_argument('--mixin_config', default= 'got10k.yaml', type=str, action='append')

    parser.add_argument('--video_path',default=gp.video_path ,type=str,help = 'path to video that you what to apply tracker')
    parser.add_argument('--output_dir', default= gp.swintrack_path + 'output_update_temp', help='path where to save, empty for no saving')

    parser.add_argument('--device', default='cuda',
                        help='device to use for training / testing')
    parser.add_argument('--seed', default=42, type=int)
    # parser.add_argument('--resume',default= swintrack_path + 'output2/SwinTrack-Tiny-mixin-g-mixin-o-mixin-t-mixin-1-mixin-0-mixin-k-mixin-.-mixin-y-mixin-a-mixin-m-mixin-l-2022.03.23-16.16.40-985342/checkpoint0000.pth', help='resume from checkpoint')
    parser.add_argument('--resume', help='resume from checkpoint')
    parser.add_argument('--num_workers', default=0, type=int)
    parser.add_argument('--checkpoint_interval', default=1, type=int)

    # distributed training parameters
    parser.add_argument('--persistent_data_workers', action='store_true', help='make the workers of dataloader persistent')
    parser.add_argument('--logging_interval', default=10, type=int)
    parser.add_argument('--enable_profile', action='store_true', help='enable profiling')
    parser.add_argument('--profile_logging_path', help='logging path of profiling, cannot be empty when enabled')
    parser.add_argument('--pin_memory', action='store_true', help='move tensors to pinned memory before transferring to GPU')
    parser.add_argument('--enable_autograd_detect_anomaly', action='store_true', help='enable the anomaly detection for the autograd engine')
    parser.add_argument('--wandb_run_offline', default= True, action='store_true', help='run wandb offline')

    parser.add_argument('--do_sweep', action='store_true')
    parser.add_argument('--sweep_config', type=str)


    parser.add_argument('--run_id', type=str)

    parser.add_argument('--master_address', type=str, default='127.0.0.1')
    parser.add_argument('--distributed_node_rank', type=int, default=0)
    parser.add_argument('--distributed_nnodes', type=int, default=1)
    parser.add_argument('--distributed_nproc_per_node', type=int, default=1)
    parser.add_argument('--distributed_do_spawn_workers', action='store_true')

    parser.add_argument('--conf_seed', default=42, type=int)
    parser.add_argument('--wandb_distributed_aware', default=False, action='store_true')

    parser.add_argument('--debug', action='store_true')

    parser.add_argument('--kill_other_python_processes', action='store_true')

    return parser
