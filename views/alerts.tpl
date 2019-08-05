% rebase('base.tpl', title='Page Title')

<body class="fixed-sn white-skin">

  
  <!-- Main layout -->
  <main>
    <div class="container-fluid">

      <div class="card text-center mb-5 py-5">

        <div class="card-body">

          <h4 class="mb-4 dark-grey-text font-weight-bold"><strong>Tipos</strong></h4>


          <!-- Info message -->
          <a class="btn btn-info" onclick="toastr.info('Hi! I am info message.');">Info message</a>

          <!-- Warning message -->
          <a class="btn btn-warning" onclick="toastr.warning('Hi! I am warning message.');">Warning message</a>

          <!-- Success message -->
          <a class="btn btn-success" onclick="toastr.success('Hi! I am success message.');">Success message</a>

          <!-- Error message -->
          <a class="btn btn-danger" onclick="toastr.error('Hi! I am error message.');">Error message</a>

        </div>

      </div>

      <div class="card text-center mb-5 py-5">

        <div class="card-body">

          <h4 class="mb-4 dark-grey-text font-weight-bold"><strong>Posição</strong></h4>


          <div class="mb-4">

            <a class="btn btn-indigo" onclick="toastr.info('Hi! Eu sou uma mensagem de informacao.', '', {positionClass: 'md-toast-top-left'});">Top
              left</a>

            <a class="btn btn-indigo" onclick="toastr.info('Hi! I am info message.', '', {positionClass: 'md-toast-top-center'});">Top
              center</a>

            <a class="btn btn-indigo" onclick="toastr.info('Hi! I am info message.', '', {positionClass: 'md-toast-top-right'});">Top
              right</a>

          </div>

          <div class="mb-4">

            <a class="btn btn-indigo" onclick="toastr.info('Hi! I am info message.', '', {positionClass: 'md-toast-bottom-left'});">Bottom
              left</a>

            <a class="btn btn-indigo" onclick="toastr.info('Hi! I am info message.', '', {positionClass: 'md-toast-bottom-center'});">Bottom
              center</a>

            <a class="btn btn-indigo" onclick="toastr.info('Hi! I am info message.', '', {positionClass: 'md-toast-bottom-right'});">Bottom
              right</a>

          </div>

        </div>

      </div>


    </div>
  </main>
