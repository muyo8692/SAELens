from sae_lens import LanguageModelSAERunnerConfig, SAETrainingRunner

cfg = LanguageModelSAERunnerConfig(
    architecture="jumprelu",
    model_name="gemma-2b",
    model_class_name="HookedTransformer",
    hook_name="blocks.12.hook_resid_post",
    hook_eval="NOT_IN_USE",
    hook_layer=12,
    hook_head_index=None,
    dataset_path="HuggingFaceFW/fineweb",
    dataset_trust_remote_code=True,
    streaming=True,
    is_dataset_tokenized=False,
    context_size=1024,
    use_cached_activations=False,
    cached_activations_path=None,
    d_in=2048,
    d_sae=16384,  # gemma scope has a width of 16.4k
    b_dec_init_method="zeros",  # initialized to all zeros according to Anthropic
    activation_fn="relu",
    normalize_sae_decoder=True,  # throughout training, we restrict the columns of W_dec to have unit norm by renormalizing after every update
    noise_scale=0.0,
    from_pretrained_path=None,
    apply_b_dec_to_input=True,  # During training, we parameterise the SAE using a pre-encoder bias Bricken et al. (2023), subtracting b_dec from activations before the encoder
    decoder_orthogonal_init=False,
    decoder_heuristic_init=False,  # We initialize W_dec using He-uniform initialization and rescale each latent vector to be unit norm
    init_encoder_as_decoder_transpose=True,  # W_enc is initalized as the transpose of W_dec, but they are not tied afterwards
    n_batches_in_buffer=64,
    training_tokens=4000000000,
    finetuning_tokens=0,
    store_batch_size_prompts=8,
    train_batch_size_tokens=4096,  # a batch size of 4,096
    normalize_activations="expected_average_only_in",  # During training, activation vectors are normalized by a fixed scalar
    device="cuda",
    act_store_device="cpu",
    seed=42,
    dtype="torch.float32",
    prepend_bos=True,
    jumprelu_init_threshold=0.001,
    jumprelu_bandwidth=0.001,
    autocast=True,
    autocast_lm=True,
    compile_llm=False,
    llm_compilation_mode="default",
    compile_sae=False,
    sae_compilation_mode=None,
    adam_beta1=0,
    adam_beta2=0.999,
    mse_loss_normalization=None,
    l1_coefficient=5.0,  # A reasonable default for λ is 5" when discussing L1 penalties
    l0_lambda=6e-4,
    lp_norm=1.0,
    scale_sparsity_penalty_by_decoder_norm=False,
    l1_warm_up_steps=0,
    l0_warm_up_steps=0,
    lr=7e-05,
    lr_scheduler_name="cosineannealing",
    lr_warm_up_steps=1000,
    lr_end=7e-06,
    lr_decay_steps=0,
    finetuning_method=None,
    use_ghost_grads=False,
    feature_sampling_window=2000,
    dead_feature_window=1000,
    dead_feature_threshold=1e-08,
    n_eval_batches=10,
    eval_batch_size_prompts=1,
    log_to_wandb=True,
    log_activations_store_to_wandb=False,
    log_optimizer_state_to_wandb=False,
    wandb_project="gemma_2b_reproduce",
    wandb_id=None,
    run_name="sae-gemma-2b-jumprelu-sc-0-norm",
    wandb_entity=None,
    wandb_log_frequency=50,
    eval_every_n_wandb_logs=10,
    resume=False,
    n_checkpoints=0,
    checkpoint_path="checkpoints/0bzfiqi2/konwqovz/g2ydv7jo",
    verbose=True,
    model_kwargs={},
    model_from_pretrained_kwargs={},
)

sparse_autoencoder = SAETrainingRunner(cfg).run()
