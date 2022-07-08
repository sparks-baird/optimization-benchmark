from optimization_benchmark import PseudoCrab

pc = PseudoCrab()

for fold in pc.folds:
    train_val_df = pc.get_train_and_val_data(fold)
