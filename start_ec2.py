importar  boto3
región  =  'us-este-1'
instancias  = [ 'identificador-instancia' , 'identificador-instancia' ]
ec2  =  boto3 . cliente ( 'ec2' , nombre_región = región )
def  lambda_handler ( evento , contexto ):
    ec2 . start_instances ( InstanciaIds = instancias )
    print ( 'comenzó sus instancias: ' +  str ( instancias ))
