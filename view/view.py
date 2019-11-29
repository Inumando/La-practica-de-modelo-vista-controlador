
class View:
    """
    ***************
    * User Methods*
    ***************
    """

    def show_all_products(self, lista, b):
        if b:
            print('There are %i users in my DB. Here they are: '% len(lista))
        print('_*_*_*_*_*_*_*_USER LIST_*_*_*_*_*_*_')
        for users in lista:
            details = str(product.id_product)+' '+product.name+' '+product.brand+' '+product.category+' '+str(product.price)+' '+ \
                str(product.weight)+' '+product.batch
            print('+ '+details)
        print('_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')

    """
    ****************
    * Movie Methods*
    ****************
    """

    """
    ***************
    * Sala Methods*
    ***************
    """

    """
    *********************
    * Billboard Methods *
    *********************
    """

    """
    *****************
    * Ticket Methods*
    *****************
    """