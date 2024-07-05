<script>
  import "iconify-icon";
</script>

<svelte:head>
  <title>Imgtools</title>
</svelte:head>

<div>
  <div class="h-screen flex items-center justify-center">
    <div class="grid grid-cols-3 gap-9 text-5xl">
      <div>
        <a href="/jpg" class="selection-menu"
          ><iconify-icon icon="hugeicons:jpg-01" style="color: #0c3d26"
          ></iconify-icon></a
        >
      </div>
      <div>
        <a href="/png" class="selection-menu"
          ><iconify-icon icon="hugeicons:png-02" style="color: #0c3d26"
          ></iconify-icon></a
        >
      </div>
      <div>
        <a href="/webp" class="selection-menu"
          ><iconify-icon icon="iconoir:webp-format" style="color: #0c3d26"
          ></iconify-icon></a
        >
      </div>
    </div>
  </div>
</div>
