class Course:
    # Outra forma : carregar apenas as indicaçõs de configuraçõs 
    # e subpartes e carregar o conteudo quando requerido pelo algoritmo
    def __init__(self,idx,configx):
        self.configs = configx
        self.courseid = idx