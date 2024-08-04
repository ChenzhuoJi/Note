def print_models(unprinted_designs,completed_models):
    
    #Page 128
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)
        
        
def show_completed_models(completed_models):
        
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
    #创建列表，包含一些要打印的设计
unprinted_designs=['phone case','robot pendant','dodecahedred']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models) 