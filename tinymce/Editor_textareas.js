/**
 * Created by maxwell on 1/13/14.
 */
tinyMCE.init({
    mode : "textareas",
    theme : "advanced",
    plugins : "autolink,lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave,visualblocks",

    theme_advanced_buttons1 : "bold,italic,underline,separator,justifyleft,justifycenter,justifyright, separator,formatselect",
    theme_advanced_buttons2 : "hr,separator,bullist,numlist,separator,outdent,indent,separator,undo,redo,separator,link,cleanup,code,separator,print,",
    theme_advanced_buttons3 : "",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    //theme_advanced_statusbar_location : "bottom",
    width: "450",
    height: "600",
    language: "{{ language }}"
});