from zope.interface import Interface


class IView(Interface):

    def __init__(context, request):  # noqa: N805
        '''
        '''

    async def __call__(self):
        '''
        '''


class ITraversableView(IView):

    async def publish_traverse(traverse_to):  # noqa: N805
        '''
        '''


class IDownloadView(IView):
    pass


class IGET(IView):
    pass


class IPUT(IView):
    pass


class IPOST(IView):
    pass


class IPATCH(IView):
    pass


class IDELETE(IView):
    pass


class IOPTIONS(IView):
    pass


class IHEAD(IView):
    pass


class ICONNECT(IView):
    pass
